import React from "react";
import Header from "../../Components/Header/Header";
import { Link, Route, useNavigate } from "react-router-dom";
import "./LoginPage.css";
import "../../Components/ButtonWide/ButtonWide.css";
import "../../Components/InputBox/InputBox.css";
import { Form, Input, Button, Checkbox } from "antd";

export default function LoginCompoment() {
  const navigate = useNavigate();

  const onFinish = (values) => {
    console.log("Success:", values);
    navigate("/foodPage");
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  const onClickSignUp = () => {
    navigate("/signUp");
  };

  return (
    <div>
      <Header headerText="Sign In" />
      <h2 className="loginText">Welcome to Calorie Shop!</h2>
      <Form
        style={{ marginLeft: "10%", marginRight: "10%" }}
        name="basic"
        layout="vertical"
        initialValues={{
          remember: true,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[
            {
              required: true,
              message: "Please input your username!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[
            {
              required: true,
              message: "Please input your password!",
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item
          name="remember"
          valuePropName="checked"
          wrapperCol={{
            offset: 12,
            span: 16,
          }}
        >
          <Checkbox>Remember me</Checkbox>
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" className="btnWide">
            Sign In
          </Button>
        </Form.Item>

        <Form.Item>
          <Button type="primary" className="btnWide" onClick={onClickSignUp}>
            Sign Up with Email
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
