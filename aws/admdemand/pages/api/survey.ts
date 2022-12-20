import { NextApiRequest, NextApiResponse } from 'next';
import { Answer } from '../../interfaces/answer';

const handler = async (_req: NextApiRequest, res: NextApiResponse) => {
    const { method, body } = _req;
    const { name, answers } = body;

    const company_size = answers[0]
    const accounting = answers[1]
    const creative = answers[2]
    const it = answers[3]

    if (method === "POST") {
        const ans: Answer = {
            name: name,
            company_size: company_size,
            accounting_size: accounting,
            creative_size: creative,
            it_size: it
        }

        console.log("Recevied request at /api/survey")

        const response = await fetch('http://localhost:3000/api/checkvalid', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(ans)
        });

        const valid = response.status
        if (valid == 200) {

            const generate_response = await fetch('http://localhost:3000/api/generate', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(ans)
            })

            const recommendation = await generate_response.json()
            res.status(200).send(JSON.stringify(recommendation));
            return

        } else {
            console.log("Answer is invalid: " + response.status)
        }

    } else {
        res.status(400).send({ "message": "Wrong method" })
    }
}

export default handler;