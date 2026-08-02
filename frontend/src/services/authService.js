import axios from "axios";

const API = "http://localhost:8000/api/v1/auth";

export async function login(username, password) {
    const form = new URLSearchParams();

    form.append("username", username);
    form.append("password", password);

    const response = await axios.post(
        `${API}/login`,
        form,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );

    return response.data;
}

export async function getCurrentUser(token) {
    const response = await axios.get(
        `${API}/me`,
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );

    return response.data;
}
