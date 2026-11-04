// Ponte verso onnxruntime-web caricato come script classico (window.ort)
const o = window.ort;
export const env = o.env;
export const Tensor = o.Tensor;
export const InferenceSession = o.InferenceSession;
export default o;
