import React, { Component } from "react";
import {
  Button,
  Form,
  Input,
  InputNumber,
  Checkbox,
  Select,
  DatePicker,
} from "antd";
import Header from "../../Components/Header/Header";
import "./GetUserInfoPage.css";
import "../../Components/ButtonWide/ButtonWide.css";
import { useNavigate } from "react-router-dom";

export default function GetUserInfoPage() {
  const { Option } = Select;
  const navigate = useNavigate();

  const onFinish = (values) => {
    const processedValues = {
      ...values,
      birthday: values["birthday"].format("YYYY-MM-DD"),
    };
    console.log("Success:", processedValues);
    navigate("/foodPage");
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
          label="Birthday"
          name="birthday"
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
