import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { Divider, Button, Skeleton, List } from "antd";
import axios from "axios";
import Header from "../../Components/Header/Header";
import FoodInfoList from "../../Components/FoodInfoList/FoodInfoList";
import RecommendedFoodInfo from "../../Components/FoodInfoList/RecommendedFoodInfo";
import CalorieInfoBlock from "../../Components/FoodInfoList/CalorieInfoBlock";
import NutritionInfoBlock from "../../Components/FoodInfoList/NutritionInfoBlock";
import JsonText from "../../Example_JSON/FOOD_INFO_EXAMPLE.json";
import "./FoodPage.css";

export default function FoodPage() {
  let totalCalorie = 0;
  let totalCarbo = 0;
  let totalProtein = 0;
  let totalFat = 0;
  let navigate = useNavigate();
  const { state } = useLocation();
  const { userID, date } = state;

  const [foodData, setFoodData] = useState([]);
  const [recommendFoodData, setRecommendFoodData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  async function getInfo() {
    await axios
      .post("/getDietLogs/" + userID, { date: date })
      .then(function (response) {
        if (response.data.isNone) {
          setFoodData([]);
        } else {
          setFoodData(response.data);
        }
      });
    await axios
      .post("/recomandationFoods/" + userID, { date: date })
      .then(function (response) {
        if (response.data.isNone) {
          setRecommendFoodData([]);
        } else {
          setRecommendFoodData(response.data);
        }
      });
    setIsLoading(false);
  }

  useEffect(() => {
    getInfo();
  }, []);

  foodData.map((item) => {
    totalCalorie += item.calorie_cost;
    totalCarbo += item.carbohydrate;
    totalProtein += item.protein;
    totalFat += item.fat;
  });
  totalCalorie = Math.round(totalCalorie * 100) / 100;

  return (
    <div className="FoodInfoPg">
      <Header headerText="Food Information" />
      <Skeleton
        avatar
        loading={isLoading}
        paragraph={{ rows: 20 }}
        style={{
          marginLeft: "5%",
          marginRight: "5%",
          marginTop: "10%",
          width: "90%",
        }}
        active
      >
        <Divider> Food Information </Divider>
        <FoodInfoList foodInfo={foodData} date={date} userID={userID} />
        <Divider> Calorie Data </Divider>
        <CalorieInfoBlock totalCalorie={totalCalorie} />
        <Divider> Nutrition Data </Divider>
        <NutritionInfoBlock
          totalCarbo={totalCarbo}
          totalFat={totalFat}
          totalProtein={totalProtein}
        />
        <Divider> Recommended Food </Divider>
        <List
          bordered
          style={{ backgroundColor: "white" }}
          dataSource={recommendFoodData}
          renderItem={(item) => (
            <List.Item>
              <RecommendedFoodInfo
                foodInfo={item}
                date={date}
                userID={userID}
              />
            </List.Item>
          )}
        />
        <Button
          type="primary"
          style={{ width: "100%", height: "50px", marginTop: "3%" }}
          onClick={() => {
            navigate("/foodDetailPage", {
              state: { isAdd: true, foodInfo: {}, date: date, userID: userID },
            });
          }}
        >
          Add more food
        </Button>
        <Button
          type="primary"
          style={{ width: "100%", height: "50px", marginTop: "3%" }}
          onClick={() => {
            navigate("/foodCustomPage", {
              state: { isAdd: true, foodInfo: {}, date: date, userID: userID },
            });
          }}
        >
          Add custom food
        </Button>
      </Skeleton>
    </div>
  );
}
