import mongoose from "mongoose";

interface DeviceAttrs {
    uuid: string;
};

interface DeviceDoc extends mongoose.Document {
    uuid: string;
};

interface DeviceModel extends mongoose.Model<DeviceDoc> {
    build(attrs: DeviceAttrs): DeviceDoc;
};

const deviceSchema = new mongoose.Schema({
    uuid: {
        type: String,
        required: true
    }
});

deviceSchema.set('toJSON', {
    transform(doc: any, ret: any) {
        ret.id = ret._id;
        delete ret._id;
        delete ret.__v;
    }
})

deviceSchema.statics.build = (attrs: DeviceAttrs) => {
    return new Device(attrs);
}
const Device = mongoose.model<DeviceDoc, DeviceModel>('Device', deviceSchema);

export { Device };