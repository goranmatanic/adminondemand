import app from './app';
import mongoose from 'mongoose';


app.listen(3000, () => {
    try {
        mongoose.connect('mongodb://adminondemand:GTGWLsbIOrn1XHZYNaAK979RbkLZByS6DH1WsmygHdOT3EhdC1NOiC63bBiTVndBmHumze1rkiVrZhrWUOF7CQ%3D%3D@adminondemand.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@adminondemand@', (err) => {
            if (err != null) {
                console.error(err);
                return;
            } else {
                console.log("Connected to database");
            }
        })
    } catch (error) {
        console.log(error)
    }
    console.log("App is listening on port: ", 3000)
});