import React from "react";
import { useNavigate } from "react-router-dom";
import { Divider, Button, Affix } from "antd";
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
  JsonText.map((item) => {
    totalCalorie += item.calorie_cost;
    totalCarbo += item.carbohydrate;
    totalProtein += item.protein;
    totalFat += item.fat;
  });
  totalCalorie = Math.round(totalCalorie * 100) / 100;

  return (
    <div className="FoodInfoPg">
      <Header headerText="Food Information" />
      <FoodInfoList foodInfo={JsonText} />
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
              state: { isAdd: true, foodInfo: {} },
            });
          }}
        >
          Add more food
        </Button>
      </Affix>
    </div>
  );
}
