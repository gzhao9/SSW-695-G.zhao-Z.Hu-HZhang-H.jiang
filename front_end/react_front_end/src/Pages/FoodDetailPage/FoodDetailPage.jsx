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
import { useLocation, useNavigate } from "react-router-dom";
import Header from "../../Components/Header/Header";
import axios from "axios";

export default function FoodDetailPage() {
  const { state } = useLocation();
  const { date, userID, isAdd, foodInfo } = state;
  const calorieRef = useRef();
  const carboRef = useRef();
  const proteinRef = useRef();
  const fatRef = useRef();
  const unitRef = useRef();
  const { Option } = Select;
  const [options, setOptions] = useState([]);
  const [fetchedData, setFetchedData] = useState([]);
  const [foodData, setFoodData] = useState({});
  const [manuallyInput, setManuallyInput] = useState(true);
  // const [calorieVal, setCalorieVal] = useState(0);
  // const [proteinVal, setProteinVal] = useState(0);
  // const [carboVal, setCarboVal] = useState(0);
  // const [fatVal, setFatVal] = useState(0);
  const navigate = useNavigate();

  let t = null;

  const onSearch = (searchText) => {
    if (t !== null) {
      clearTimeout(t);
    }
    t = setTimeout(() => {
      searchFood(searchText);
    }, 500);
  };

  const onSelect = (data) => {
    console.log("onSelect", data);
    fetchedData.map((item) => {
      if (item.foodName === data) {
        setFoodData(item);
      }
    });
  };

  function searchFood(keywords) {
    if (keywords === "") {
      return;
    }
    axios
      .post("/serach_food_result/" + userID, { keywords: keywords })
      .then((response) => {
        let data = response.data;

        if (data === null) {
          setOptions([]);
          setFetchedData([]);
        } else {
          let tmp = new Array();

          data.map((item) => {
            tmp.push({ key: item.foodId, value: item.foodName });
          });
          setOptions(tmp);
          setFetchedData(data);
        }
      });
  }

  function onFinish(values) {
    let processedData = {
      // isAdd: isAdd,
      userId: userID,
      Date: date,
      foodId: foodData.foodId,
      unit: values.unit,
      manuallyInput: values.manuallyInput,
      mealType: values.type,
      foodInfo: {
        energy: values.calorie_rate,
        carbohydrate: values.carbohydrate,
        fat: values.fat,
        protein: values.protein,
        foodName: values.foodName,
      },
    };
    axios.post("/updateDietInfo/" + userID, processedData).then((response) => {
      navigate("/userInfoPage", { state: { userID: userID, date: date } });
    });
  }

  function onFinishFailed(errorInfo) {
    console.log("Failed:", errorInfo);
  }

  function onUnitChange(value) {
    if (foodData === null) {
      return;
    }
    const { energy, carbohydrate, protein, fat } = foodData;
    // setCalorieVal(energy * value);
    // setCarboVal(carbohydrate * value);
    // setFatVal(fat * value);
    // setProteinVal(protein * value);
    calorieRef.current.value = energy * value;
    proteinRef.current.value = protein * value;
    fatRef.current.value = fat * value;
    carboRef.current.value = carbohydrate * value;
  }

  function switchManuallyInput(checked) {
    setManuallyInput(!checked);
  }

  useEffect(() => {
    console.log(foodData);
  }, [foodData]);

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
            ref={unitRef}
            precision={2}
            onChange={onUnitChange}
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
          <Switch
            style={{ float: "left" }}
            onChange={switchManuallyInput}
            disabled
          />
        </Form.Item>

        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Calorie (kcal)"
          name="calorie_rate"
          initialValue={state.foodInfo.calorie_cost}
          // rules={[
          //   {
          //     required: true,
          //     message: "Please input the calorie!",
          //   },
          // ]}
        >
          <InputNumber
            style={{ float: "left" }}
            ref={calorieRef}
            // value={calorieVal}
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
          // rules={[
          //   {
          //     required: true,
          //     message: "Please input the carbohydrate!",
          //   },
          // ]}
        >
          <InputNumber
            style={{ float: "left" }}
            ref={carboRef}
            // value={carboVal}
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
          // rules={[
          //   {
          //     required: true,
          //     message: "Please input the protein!",
          //   },
          // ]}
        >
          <InputNumber
            style={{ float: "left" }}
            ref={proteinRef}
            // value={proteinVal}
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
          // rules={[
          //   {
          //     required: true,
          //     message: "Please input the fat!",
          //   },
          // ]}
        >
          <InputNumber
            style={{ float: "left" }}
            ref={fatRef}
            // value={fatVal}
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
