/* eslint-disable @typescript-eslint/no-explicit-any */
export interface HeaderType {
    [key: string]: any;
}

export interface RequestInterface {
    method: string;
    route: string;
    headers?: HeaderType;
    [key: string]: any;
}
  
export interface AxiosInterface {
    method: string;
    url: string;
    [key: string]: any;
}