import axios from "axios";

export default axios.create({
    baseURL: "https://api-grownsave.ai-softdev.com/",
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});