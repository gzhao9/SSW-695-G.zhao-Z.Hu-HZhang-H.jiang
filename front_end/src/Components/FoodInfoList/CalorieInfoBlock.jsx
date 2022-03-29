import React from "react";

export default function CalorieInfoBlock(props) {
  const { totalCalorie } = props;
  return (
    <div>
      <p
        className="foodNameText"
        style={{ color: "#2F4F4F", fontSize: "18px" }}
      >
        Total Calorie:
      </p>
      <p
        className="foodCalorieText"
        style={{ color: "#2F4F4F", fontSize: "18px" }}
      >
        {totalCalorie} kcal
      </p>
    </div>
  );
}
