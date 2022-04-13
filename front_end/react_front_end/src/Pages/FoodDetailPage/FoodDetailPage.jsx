import React, { useState, useRef, useEffect } from "react";
import {
  Button,
  Form,
  Input,
  InputNumber,
  Switch,
  AutoComplete,
  Select,
} from "antd";
import { useLocation } from "react-router-dom";
import Header from "../../Components/Header/Header";
import axios from "axios";

export default function FoodDetailPage() {
  const { state } = useLocation();
  const { date, userID, isAdd, foodInfo } = state;
  const calorieRef = useRef();
  const carboRef = useRef();
  const proteinRef = useRef();
  const fatRef = useRef();
  const { Option } = Select;
  const [options, setOptions] = useState([]);
  const [manuallyInput, setManuallyInput] = useState(true);

  const mockVal = (str, repeat = 1) => ({
    value: str.repeat(repeat),
  });

  const onSearch = (searchText) => {
    setOptions(
      !searchText
        ? []
        : [mockVal(searchText), mockVal(searchText, 2), mockVal(searchText, 3)]
    );
  };

  const onSelect = (data) => {
    console.log("onSelect", data);
  };

  function onFinish(values) {
    console.log("Success:", values);
    let processedData = {
      isAdd: isAdd,
      userID: userID,
      Date: date,
      foodID: 0,
      manuallyInput: values.manuallyInput,
      Type: values.type,
      foodInfo: {
        calorie_rate: values.calorie_rate,
        carbohydrate: values.carbohydrate,
        fat: values.fat,
        protein: values.protein,
        foodName: values.foodName,
      },
    };
    console.log(processedData);
    axios.post("/updateDietInfo/" + userID, processedData);
  }

  function onFinishFailed(errorInfo) {
    console.log("Failed:", errorInfo);
  }

  function switchManuallyInput(checked) {
    setManuallyInput(!checked);
  }

  useEffect(() => console.log(state.date), []);

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
      >
        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Food Name"
          name="foodName"
          initialValue={state.foodInfo.food_name}
          rules={[
            {
              required: true,
              message: "Please input the food name!",
            },
          ]}
        >
          <AutoComplete
            options={options}
            onSearch={onSearch}
            onSelect={onSelect}
          />
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
          <Select style={{ float: "left" }}>
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
          label="Manually Input"
          name="manuallyInput"
          valuePropName="checked"
          initialValue={false}
        >
          <Switch style={{ float: "left" }} onChange={switchManuallyInput} />
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
            ref={calorieRef}
            disabled={manuallyInput}
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
            ref={carboRef}
            disabled={manuallyInput}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Protein (kcal)"
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
            ref={proteinRef}
            disabled={manuallyInput}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Fat (kcal)"
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
            ref={fatRef}
            disabled={manuallyInput}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>

        <br />

        <Form.Item
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
        {!state.isAdd ? (
          <Form.Item
            wrapperCol={{
              offset: 0,
              span: 16,
            }}
          >
            <Button
              type="primary"
              style={{
                width: "80%",
                height: "50px",
                borderRadius: "25px",
                bottom: "20px",
              }}
            >
              Delete Food
            </Button>
          </Form.Item>
        ) : null}
      </Form>
    </div>
  );
}
