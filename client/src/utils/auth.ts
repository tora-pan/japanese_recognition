export const setAuthenticationResult = async (
    authResult: any
) => {
    const {token} = authResult;
    sessionStorage.setItem("AccessToken", token);
    return true;
}


export const isAuthenticated = () => {
    console.log('isAuthenticated', sessionStorage.getItem("AccessToken"));
    return sessionStorage.getItem("AccessToken");
}


export const logout = () => {
    sessionStorage.removeItem("AccessToken");
    return true
}


export const getSession = async () => {
    return sessionStorage.getItem("IdToken");
}