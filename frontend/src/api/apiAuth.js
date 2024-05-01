import axios from "axios";

const root = "http://localhost:8000";
const loginEndpoint = "/api/v1/auth/login/";
const logoutEndpoint = "/api/v1/auth/logout/";

export async function apiSilantlogin(login, password) {
    const responseData = await axios({
        method: "POST",
        url: `${root}${loginEndpoint}`,
        data: {
            login: login,
            password: password
        }
    }).then(
        (response) => {
            console.log("silantlogin", response.status, response.data);
            if (response.status === 200) {
                return response.data;
            }
            else {
                return response.data;
            }
        }
    ).catch(
        (error) => {
            console.log(`Error: ${error}`);
        }
    );
    return responseData;
};


export async function apiSilantLogout(token) {
    const responseData = await axios({
        method: "POST",
        url: `${root}${logoutEndpoint}`,
        data: {
            token: token
        }
    }).then(
        (response) => {
            console.log("silantLogout", response.status, response.data);
            return response.data;
        }
    ).catch(
        (error) => {
            console.log(`Error: ${error}`);
        }
    );
    return responseData;
};