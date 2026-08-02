import {
    createContext,
    useContext,
    useEffect,
    useState,
} from "react";

import {
    login,
    getCurrentUser,
} from "../services/authService";

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {
        restoreSession();
    }, []);

    async function restoreSession() {
        const token = localStorage.getItem("token");

        if (!token) {
            setLoading(false);
            return;
        }

        try {
            const currentUser = await getCurrentUser(token);

            setUser(currentUser);
        } catch (err) {
            console.error(err);

            localStorage.removeItem("token");
        }

        setLoading(false);
    }

    async function signIn(
        username,
        password,
    ) {
        const result = await login(
            username,
            password,
        );

        localStorage.setItem(
            "token",
            result.access_token,
        );

        const currentUser =
            await getCurrentUser(
                result.access_token,
            );

        setUser(currentUser);
    }

    function signOut() {
        localStorage.removeItem("token");

        setUser(null);
    }

    return (
        <AuthContext.Provider
            value={{
                user,
                loading,
                signIn,
                signOut,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    return useContext(AuthContext);
}