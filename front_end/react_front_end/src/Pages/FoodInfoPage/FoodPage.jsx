import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { Divider, Button, Affix } from "antd";
import axios from "axios";
import Header from "../../Components/Header/Header";
import FoodInfoList from "../../Components/FoodInfoList/FoodInfoList";
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

  useEffect(() => {
    axios
      .post("/getDietLogs/" + userID, { date: date })
      .then(function (response) {
        if (response.data.isNone) {
          setFoodData([]);
        } else {
          setFoodData(response.data);
        }
        console.log(response.data);
      });
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
      <FoodInfoList foodInfo={foodData} date={date} userID={userID} />
      <Divider> Calorie Data </Divider>
      <CalorieInfoBlock totalCalorie={totalCalorie} />
      <Divider> Nutrition Data </Divider>
      <NutritionInfoBlock
        totalCarbo={totalCarbo}
        totalFat={totalFat}
        totalProtein={totalProtein}
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
    </div>
  );
}
