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
        if (response.data[0].isNone) {
          setFoodData([]);
        } else {
          setFoodData(response.data);
        }
      });
    // setFoodData([
    //   {
    //     food_name: "cookie",
    //     type: "B",
    //     weight: 254,
    //     carbohydrate: 25,
    //     protein: 45,
    //     fat: 15,
    //     calorie_cost: 635,
    //   },
    //   {
    //     food_name: "apple",
    //     type: "LA",
    //     weight: 122,
    //     carbohydrate: 11,
    //     protein: 22,
    //     fat: 33,
    //     calorie_cost: 444,
    //   },
    //   {
    //     food_name: "pizza",
    //     type: "D",
    //     weight: 1,
    //     carbohydrate: 2,
    //     protein: 3,
    //     fat: 4,
    //     calorie_cost: 666,
    //   },
    // ]);
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
      <Affix offsetBottom={0}>
        <Button
          type="primary"
          style={{ width: "100%", height: "50px" }}
          onClick={() => {
            navigate("/foodDetailPage", {
              state: { isAdd: true, foodInfo: {}, date: date, userID: userID },
            });
          }}
        >
          Add more food
        </Button>
      </Affix>
    </div>
  );
}
