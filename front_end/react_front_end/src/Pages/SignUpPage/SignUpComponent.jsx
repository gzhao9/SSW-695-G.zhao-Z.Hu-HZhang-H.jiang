import React, { Component } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Input, Button } from "antd";
import axios from "axios";
import Header from "../../Components/Header/Header";
import "../../Components/ButtonWide/ButtonWide.css";
import "./SignUpPage.css";

export default function SignUpComponent() {
  const navigate = useNavigate();

  const onFinish = (values) => {
    axios.post("/verifyRegister", values).then((response) => {
      let isSuccess = response.data["isSuccess"];
      if (isSuccess === true) {
        navigate("/getUserInfoPage", {
          state: { userID: values.userID, userData: {} },
        });
      } else {
        alert("You email address already exists!");
      }
    });
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <div>
      <Header headerText="Sign Up" />
      <h2 className="signupText">
        Start your diet meal plan with Calorie Shopping!
      </h2>
      <Form
        name="register"
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        layout="vertical"
        scrollToFirstError
        style={{ marginLeft: "10%", marginRight: "10%" }}
      >
        <Form.Item
          name="userID"
          label="E-mail"
          rules={[
            {
              type: "email",
              message: "The input is not valid E-mail!",
            },
            {
              required: true,
              message: "Please input your E-mail!",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="password"
          label="Password"
          rules={[
            {
              required: true,
              message: "Please input your password!",
            },
            () => ({
              validator(_, value) {
                if (value && (value.length < 8 || value.length > 32)) {
                  return Promise.reject(
                    new Error(
                      "The length of the password should be from 8 to 32!"
                    )
                  );
                }
                return Promise.resolve();
              },
            }),
          ]}
          hasFeedback
        >
          <Input.Password />
        </Form.Item>
        <Form.Item
          name="confirm"
          label="Confirm Password"
          dependencies={["password"]}
          hasFeedback
          rules={[
            {
              required: true,
              message: "Please confirm your password!",
            },
            ({ getFieldValue }) => ({
              validator(_, value) {
                if (!value || getFieldValue("password") === value) {
                  return Promise.resolve();
                }

                return Promise.reject(
                  new Error("The two passwords that you entered do not match!")
                );
              },
            }),
          ]}
        >
          <Input.Password />
        </Form.Item>

        <br />

        <Form.Item>
          <Button type="primary" htmlType="submit" className="btnWide">
            Start Calorie Shopping!
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
