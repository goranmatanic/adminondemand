import { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import { promises as fs } from 'fs';
import { Answer } from '../../interfaces/answer';
import { http_host } from '../../utils/sample-data';

const handler = async (_req: NextApiRequest, res: NextApiResponse) => {
    const { method, body } = _req;

    const answer: Answer = body

    const jsonDirectory = path.join(process.cwd(), 'json')
    const fileContents = await fs.readFile(jsonDirectory + '/services.json', 'utf-8');
    const file_json = JSON.parse(fileContents)


    console.log("Recevied request at /api/generate")

    const GetClosesValue = async (answer: Answer) => {
        var office_services_abs = []
        var creative_services_abs = []

        const response = await fetch(`${http_host}/api/quantify`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(answer)
        })

        const { value } = await response.json()

        file_json['services'].forEach(service => {
            if (service['category'] == "office") {
                var svc = {
                    name: service['name'],
                    url: service['url'],
                    price: service['price'],
                    abs: Math.abs(value - parseInt(service['value']))
                }
                office_services_abs.push(svc)
            }

            if (answer.creative_size != "0" && service['category'] == "creative") {
                var svc = {
                    name: service['name'],
                    url: service['url'],
                    price: service['price'],
                    abs: Math.abs(value - parseInt(service['value']))
                }
                creative_services_abs.push(svc)
            }
        });

        var sorted_offices_services = office_services_abs.sort((a, b) => a.abs - b.abs)
        var sorted_creative_services = creative_services_abs.sort((a, b) => a.abs - b.abs)
        var sorted_services = sorted_offices_services.slice(0, 3).concat(sorted_creative_services.slice(0, 3))

        return sorted_services
    }

    const recommendation = await GetClosesValue(answer)

    res.status(200).send({
        answer: answer,
        recommendation: recommendation
    })

    return
}

export default handler;