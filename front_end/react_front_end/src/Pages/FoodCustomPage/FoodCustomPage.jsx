import React, { useState, useRef, useEffect } from "react";
import { Button, Form, Input, InputNumber, Switch, Select } from "antd";
import { useLocation, useNavigate } from "react-router-dom";
import Header from "../../Components/Header/Header";
import axios from "axios";

export default function FoodCustomPage() {
  const { state } = useLocation();
  const { date, userID, isAdd, foodInfo } = state;
  const { Option } = Select;
  const navigate = useNavigate();

  function onFinish(values) {
    let processedData = {
      userId: userID,
      Date: date,
      foodId: -1,
      unit: values.unit,
      manuallyInput: true,
      mealType: values.type,
      foodInfo: {
        energy: values.calorie_rate,
        carbohydrate: values.carbohydrate,
        fat: values.fat,
        protein: values.protein,
        foodName: values.foodName,
      },
    };
    console.log(processedData);
    axios.post("/updateDietInfo/" + userID, processedData).then((response) => {
      navigate("/userInfoPage", { state: { userID: userID, date: date } });
    });
  }

  function onFinishFailed(errorInfo) {
    console.log("Failed:", errorInfo);
  }

  return (
    <div>
      <Header headerText="Food Setting" />
      <Form
        name="foodSetting"
        labelCol={{
          span: 3,
        }}
        wrapperCol={{
          span: 6,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
        layout="vertical"
      >
        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Food Name"
          name="foodName"
          rules={[
            {
              required: true,
              message: "Please input the food name!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Unit (g)"
          name="unit"
          initialValue={state.foodInfo.weight}
          rules={[
            {
              required: true,
              message: "Please input the food weight!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Type"
          name="type"
          initialValue={state.foodInfo.type}
          rules={[
            {
              required: true,
              message: "Please input the food type!",
            },
          ]}
        >
          <Select style={{ float: "left", textAlign: "left" }}>
            <Option value="B">Breakfast</Option>
            <Option value="L">Lunch</Option>
            <Option value="D">Dinner</Option>
            <Option value="BA">Additional Breakfast</Option>
            <Option value="LA">Additional Lunch</Option>
            <Option value="DA">Additional Dinner</Option>
          </Select>
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Calorie (kcal)"
          name="calorie_rate"
          initialValue={state.foodInfo.calorie_cost}
          rules={[
            {
              required: true,
              message: "Please input the calorie!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Carbohydrate (g)"
          name="carbohydrate"
          initialValue={state.foodInfo.carbohydrate}
          rules={[
            {
              required: true,
              message: "Please input the carbohydrate!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Protein (g)"
          name="protein"
          initialValue={state.foodInfo.protein}
          rules={[
            {
              required: true,
              message: "Please input the protein!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Fat (g)"
          name="fat"
          initialValue={state.foodInfo.fat}
          rules={[
            {
              required: true,
              message: "Please input the fat!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <br />

        <Form.Item
          style={{ marginTop: "10%" }}
          wrapperCol={{
            offset: 0,
            span: 16,
          }}
        >
          <Button
            type="primary"
            htmlType="submit"
            style={{
              width: "80%",
              height: "50px",
              borderRadius: "25px",
              bottom: "20px",
            }}
          >
            {state.isAdd ? "Add Food" : "Change Food Info"}
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
