import axios from "axios";
import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { setAuthenticationResult } from "../../utils/auth";
import styled from "styled-components";
// import Cookies from "js-cookie";

const LoginPage = () => {
  const GlassDiv = styled.div`
    width: 70%;
    margin: 40px auto;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 2rem;
  `;

  const StyledForm = styled.form`
    font-family: "Poppins", sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
  `;

  const StyledInput = styled.input`
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin: 8px 0px;
    font-size: 14px;
    font-weight: 300;
  `;

  const StyledButton = styled.button`
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
  `;

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
  };

  const navigate = useNavigate();

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    console.log('event', event);

    const data = new FormData(event.currentTarget);

    const username = String(data.get("username"));

    const password = String(data.get("password"));

    if (username && password) {
      login(username, password).then(async (response) => {
        if (response && response.data) {
          await setAuthenticationResult(response.data);
          navigate("/");
        }
      });
    }
  };

  return (
    <GlassDiv>
      <StyledForm onSubmit={handleSubmit}>
        <label>Username</label>
        <StyledInput type="text" placeholder="Email or Phone" name="username" />
        <label>Password</label>
        <StyledInput type="password" placeholder="Password" name="password" />
        <StyledButton>Log In</StyledButton>
      </StyledForm>
    </GlassDiv>
  );
};

export default LoginPage;
