import axios, { AxiosResponse } from "axios";
import { AxiosInterface, RequestInterface } from "../global.d"


export async function MakeRequest({
  method,
  route,
  headers,
  data,
}: RequestInterface) {
  const regex: RegExp = /^\//;

  if (!regex.test(route)) {
    throw new Error("misconfigured route, it needs to start with a forward slash")
  }

  const token = sessionStorage.getItem("AccessToken") || "test";

  const requestConfig: AxiosInterface = {
    method: method,
    url: `http://localhost:8003${route}`,
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,
      ...headers,
    },
  };

  console.log(requestConfig);

  if (data) requestConfig.data = data;

  try {
    const apiResponse: AxiosResponse = await axios(requestConfig);
    return apiResponse.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response) {
        if (error.response.status === 401) return document.location.href = "/login";
      }
    }
    throw error;
  }
}