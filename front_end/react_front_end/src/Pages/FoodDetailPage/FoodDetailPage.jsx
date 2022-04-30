import React, { useState, useRef, useEffect } from "react";
import {
  Button,
  Form,
  Row,
  InputNumber,
  Switch,
  AutoComplete,
  Select,
  Table,
} from "antd";
import { useLocation, useNavigate } from "react-router-dom";
import Header from "../../Components/Header/Header";
import axios from "axios";

export default function FoodDetailPage() {
  const { state } = useLocation();
  const { date, userID, foodInfo } = state;
  const unitRef = useRef();
  const { Option } = Select;
  const [options, setOptions] = useState([]);
  const [fetchedData, setFetchedData] = useState([]);
  const [foodData, setFoodData] = useState({});
  const [manuallyInput, setManuallyInput] = useState(true);
  const [calorieVal, setCalorieVal] = useState(0);
  const [proteinVal, setProteinVal] = useState(0);
  const [carboVal, setCarboVal] = useState(0);
  const [fatVal, setFatVal] = useState(0);
  const [unit, setUnit] = useState(0);
  const [foodName, setFoodName] = useState("");
  const [dataSource, setDataSource] = useState([
    {
      key: "1",
      name: "Calorie",
      unit: 0,
    },
    {
      key: "2",
      name: "Carbohydrates",
      unit: 0,
    },
    {
      key: "3",
      name: "Proteins",
      unit: 0,
    },
    {
      key: "4",
      name: "Fat",
      unit: 0,
    },
  ]);
  const navigate = useNavigate();

  const tableColumn = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Unit",
      dataIndex: "unit",
      key: "unit",
    },
  ];

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
    setOptions([]);
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
    if (Object.keys(foodData).length === 0) {
      alert("Please select the food info!");
      return;
    }
    let processedData = {
      userId: userID,
      Date: date,
      foodId: foodData.foodId,
      unit: unit,
      manuallyInput: false,
      mealType: values.type,
      foodInfo: {
        energy: calorieVal,
        carbohydrate: carboVal,
        fat: fatVal,
        protein: proteinVal,
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
    setCalorieVal((energy * value) / 100.0);
    setCarboVal((carbohydrate * value) / 100.0);
    setFatVal((fat * value) / 100.0);
    setProteinVal((protein * value) / 100.0);
    setUnit(value);
  }

  useEffect(() => {
    if (foodData === null) {
      return;
    }
    const { energy, carbohydrate, protein, fat } = foodData;
    setCalorieVal((energy * unit) / 100.0);
    setCarboVal((carbohydrate * unit) / 100.0);
    setFatVal((fat * unit) / 100.0);
    setProteinVal((protein * unit) / 100.0);
    setFoodName(foodData.foodName);
  }, [foodData]);

  useEffect(() => {
    setDataSource([
      {
        key: "1",
        name: "Calorie",
        unit: Math.round(calorieVal * 100) / 100,
      },
      {
        key: "2",
        name: "Carbohydrates",
        unit: Math.round(carboVal * 100) / 100,
      },
      {
        key: "3",
        name: "Proteins",
        unit: Math.round(proteinVal * 100) / 100,
      },
      {
        key: "4",
        name: "Fat",
        unit: Math.round(fatVal * 100) / 100,
      },
    ]);
  }, [calorieVal, carboVal, fatVal, proteinVal, foodData]);

  useEffect(() => {
    console.log(foodInfo);
    if (!foodInfo) {
      return;
    }
    setFoodData(foodInfo);
  }, []);

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
          initialValue={foodInfo.foodName}
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
          <Select style={{ float: "left", textAlign: "left" }}>
            <Option value="B">Breakfast</Option>
            <Option value="L">Lunch</Option>
            <Option value="D">Dinner</Option>
            <Option value="BA">Additional Breakfast</Option>
            <Option value="LA">Additional Lunch</Option>
            <Option value="DA">Additional Dinner</Option>
          </Select>
        </Form.Item>

        <p
          style={{
            float: "left",
            marginLeft: "10%",
            marginRight: "10%",
            fontWeight: "bolder",
          }}
        >
          Chosen Food: {!foodName || foodName.length === 0 ? "None" : foodName}
        </p>

        <Table
          columns={tableColumn}
          dataSource={dataSource}
          pagination={false}
          style={{ marginLeft: "10%", marginRight: "10%" }}
        ></Table>

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
            Add Food
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
