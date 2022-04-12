import React, { Component } from "react";
import {
  Button,
  Form,
  Input,
  InputNumber,
  Checkbox,
  Select,
  DatePicker,
  Radio,
  Space,
} from "antd";
import Header from "../../Components/Header/Header";
import "./GetUserInfoPage.css";
import axios from "axios";
import moment from "moment";
import "../../Components/ButtonWide/ButtonWide.css";
import { useNavigate, useLocation } from "react-router-dom";

export default function GetUserInfoPage() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const { userID, userData } = state;
  const { Option } = Select;
  const onFinish = (values) => {
    const processedValues = {
      ...values,
      birthday: values["birthday"].format("YYYY-MM-DD"),
      date: moment().format("YYYY-MM-DD"),
    };
    console.log("Success:", processedValues);
    axios
      .post("/updateUserInfo/" + userID, processedValues)
      .then((response) => {
        navigate("/userInfoPage", { state: { userID: userID } });
      });
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };
  return (
    <div>
      <Header headerText="Input Necessary Information" />
      <Form
        name="getUserInfo"
        style={{ marginLeft: "10%", marginRight: "10%", marginTop: "10%" }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
        layout="vertical"
        initialValues={{ isVegan: false, allergySource: [] }}
      >
        <Form.Item
          label="Full Name"
          name="fullName"
          initialValue={userData.userName}
          rules={[
            {
              required: true,
              message: "Please input your name!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Gender"
          name="gender"
          initialValue={userData.gender}
          rules={[
            {
              required: true,
              message: "Please enter your gender!",
            },
          ]}
        >
          <Radio.Group size="small" style={{ float: "left" }}>
            <Space direction="vertical" size="small" align="start">
              <Radio value="male">Male</Radio>
              <Radio value="female">Female</Radio>
              <Radio value="other">Other</Radio>
            </Space>
          </Radio.Group>
        </Form.Item>

        <Form.Item
          label="Birthday"
          name="birthday"
          initialValue={
            userData.birthday
              ? moment(userData.birthday, "MM-DD-YYYY")
              : moment()
          }
          rules={[
            {
              required: true,
              message: "Please input your birthday!",
            },
          ]}
        >
          <DatePicker style={{ float: "left" }} />
        </Form.Item>

        <Form.Item
          label="Height (cm)"
          name="height"
          initialValue={userData.height}
          rules={[
            {
              required: true,
              message: "Please input your height!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={500}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          label="Weight (kg)"
          name="weight"
          initialValue={userData.weight}
          rules={[
            {
              required: true,
              message: "Please input your weight!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={1000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          label="Fat Rate (%)"
          name="fatRate"
          initialValue={userData.fatRate}
          rules={[
            {
              required: true,
              message: "Please input your fat rate!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={100}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          label="Please choose your meal plan"
          name="mealPlan"
          initialValue={userData.mealPlan}
          rules={[
            {
              required: true,
              message: "Please choose your meal plan!",
            },
          ]}
        >
          <Radio.Group size="small" style={{ float: "left" }}>
            <Space direction="vertical" size="small" align="start">
              <Radio value="keepHealth">Keep Healthy</Radio>
              <Radio value="loseWeight">Lose Weight</Radio>
              <Radio value="buildMuscle">Build Muscle</Radio>
            </Space>
          </Radio.Group>
        </Form.Item>

        <Form.Item label="I am a vegan" name="isVegan" valuePropName="checked">
          <Checkbox style={{ float: "left" }} />
        </Form.Item>

        <Form.Item label="Allergy Source" name="allergySource">
          <Select mode="multiple" optionLabelProp="label">
            <Option value="milk" label="Milk">
              Milk
            </Option>
            <Option value="eggs" label="Eggs">
              Eggs
            </Option>
            <Option value="peanuts" label="Peanuts">
              Peanuts
            </Option>
            <Option value="treenuts" label="Tree Nuts">
              Tree Nuts
            </Option>
            <Option value="soy" label="Soy">
              Soy
            </Option>
            <Option value="wheat" label="Wheat">
              Wheat
            </Option>
            <Option value="fish" label="Fish">
              Fish
            </Option>
            <Option value="shellfish" label="Shellfish">
              Shellfish
            </Option>
          </Select>
        </Form.Item>

        <br />

        <Form.Item
          wrapperCol={{
            offset: 0,
            span: 16,
          }}
        >
          <Button type="primary" htmlType="submit" className="btnWide">
            Next
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
