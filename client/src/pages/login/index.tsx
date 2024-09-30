import axios from "axios";
import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { setAuthenticationResult } from "../../utils/auth";
import Cookies from "js-cookie";

const LoginPage = () => {

  const login = async (email: string, password: string) => {
    try {
      const response = await axios.post("http://localhost:8003/auth/login/", {
        email: email,
        password: password,
      });
      console.log(response);
      return response;
    } catch (error) {
      console.log(error);
    }
  }

  const navigate = useNavigate();

    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const data = new FormData(event.currentTarget);

        const username = String(data.get('username'));

        const password = String(data.get('password'));

        if (username && password){
            login(username, password).then(
                async (response) => {
                    if (response && response.data) {
                        await setAuthenticationResult(response.data);
                        navigate("/");
                    }
                }
            )
        }
    };

  return (
    <div className="container">
      Login
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
