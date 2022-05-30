import { DefaultApi } from "./generated/api";
import { Configuration } from "./generated/configuration";

const readAccessToken = async (): Promise<string> => {
  return localStorage.getItem("token") || "";
};

export const basePath: string = "http://localhost:8000";

const apiConfig: Configuration = new Configuration({
  basePath,
  accessToken: readAccessToken,
});

export const defaultApi: DefaultApi = new DefaultApi(apiConfig);
