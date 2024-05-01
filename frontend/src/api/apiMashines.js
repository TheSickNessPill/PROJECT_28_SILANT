import axios from "axios";

const root = "http://localhost:8000";
const baseMashinesEndpoint = "/api/v1/mashines/baseMasines/";
const fullDataByUserEndpoint ="/api/v1/mashines/fullDataByUser/"

export async function apiBaseMashines(factoryNumber) {
    const responseData = await axios({
        method: "POST",
        url: `${root}${baseMashinesEndpoint}`,
        data: {
            factoryNumber: factoryNumber
        }
    }).then(
        (response) => {
            console.log("apiBaseMashines", response.status, response.data.status)
            if (response.status === 200) {
                console.log(response.data);
                return response.data;
            }
            else { return {}; }
        }
    ).catch(
        (error) => {
            console.log(`Error: ${error}`)
        }
    );

    return responseData;
};


export async function apiFullDataByUser(token, role) {
    const responseData = await axios({
        method: "POST",
        url: `${root}${fullDataByUserEndpoint}`,
        data: {
            token: token,
            role: role
        }
    }).then(
        (response) => {
            console.log("apiFullDataByUserEndpoint", response.status, response.data.status)
            return response.data;
        }
    ).catch(
        (error) => {
            console.log(`Error: ${error}`)
        }
    );
    return responseData;
};