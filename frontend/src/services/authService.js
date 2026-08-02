import api from "./api";

export async function login(username, password) {

    const form = new URLSearchParams();

    form.append("username", username);
    form.append("password", password);

    const response = await api.post(
        "/auth/login",
        form,
        {
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded",
            },
        }
    );

    return response.data;
}

export async function getCurrentUser(token) {

    const response = await api.get(
        "/auth/me",
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );

    return response.data;
}