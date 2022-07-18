import express from "express";
import mongoose from "mongoose";
import { Device } from "./models/device";

const app = express();
app.set('trust proxy', true);
app.use(express.json())

app.get('/', (req, res) => {
    res.statusCode = 200
    res.send("Hello world")
})

app.get('/testdb', (req, res) => {
    mongoose.connect('mongodb://adminondemand:GTGWLsbIOrn1XHZYNaAK979RbkLZByS6DH1WsmygHdOT3EhdC1NOiC63bBiTVndBmHumze1rkiVrZhrWUOF7CQ%3D%3D@adminondemand.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@adminondemand@', (err) => {
        if (err != null) {
            console.error(err);
            res.statusCode = 400;
            res.send("Error");
            return;
        } else {
            console.log("Connected to database");
        }
        res.statusCode = 200;
        res.send("Connected to database");
    })
})

app.post('/newdevice', async (req, res) => {
    try {
        const { uuid } = req.body;
        console.log("UUID: ", uuid);

        const existingDevice = await Device.findOne({ uuid })
        if (existingDevice) {
            res.statusCode = 403
            res.send("Device with this UUID already exists");
            return
        }

        const device = Device.build({ uuid })
        await device.save();

        res.statusCode = 200
        res.send("Your new UUID: " + uuid)
    } catch (error) {
        console.log(error)
        res.statusCode = 400
        res.send("Please add uuid to body");
    }

})

app.get('/getdevices', async (req, res) => {
    const allDevices = await Device.find({})
    res.statusCode = 200;
    res.send(allDevices);
})

app.post('/authenticate', async (req, res) => {
    try {
        const { uuid } = req.body;
        const existingDevice = await Device.findOne({ uuid })

        if (existingDevice) {
            res.statusCode = 200;
            res.send("Successfully authenticated");
            return
        } else {
            res.statusCode = 403;
            res.send("Failed to authenticate");
        }

    } catch (error) {
        res.statusCode = 400;
        res.send("Please add UUID to request body")
    }
})

app.post('/removedevice', async (req, res) => {
    try {
        const { uuid } = req.body;
        const existingDevice = await Device.findOne({ uuid })

        if (existingDevice) {

            await Device.deleteMany({ uuid: uuid })

            res.statusCode = 201;
            res.send("Device deleted")

            return
        } else {
            res.statusCode = 403;
            res.send("UUID doesn't exist");
        }

    } catch (error) {
        res.statusCode = 400;
        res.send("Please add UUID to request body")
    }
})


export default app