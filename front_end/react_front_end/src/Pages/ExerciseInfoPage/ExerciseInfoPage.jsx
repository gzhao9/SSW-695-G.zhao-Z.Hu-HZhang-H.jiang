import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import axios from "axios";
import Header from "../../Components/Header/Header";
import ExerciseInfo from "../../Components/ExerciseInfoList/ExerciseInfo";
import { List, Divider, Affix, Button } from "antd";
import "../../UniversalStyle/UniversalStyle.css";

export default function ExerciseInfoPage() {
  const { state } = useLocation();
  const { userID, date } = state;
  const [exerciseInfo, setExerciseInfo] = useState([]);
  const [totalCalorie, setTotalCalorie] = useState(0);
  const navigate = useNavigate();
  useEffect(() => {
    setExerciseInfo([
      { exercise_name: "Run", minute: 30, calorie: 100 },
      { exercise_name: "Walk", minute: 30, calorie: 100 },
      { exercise_name: "Baseball", minute: 30, calorie: 100 },
      { exercise_name: "Basketball", minute: 30, calorie: 100 },
    ]);
  }, []);

  useEffect(() => {
    let tmp = 0;
    // console.log(exerciseInfo);
    exerciseInfo.map((item) => {
      tmp += item.calorie;
    });
    setTotalCalorie(tmp);
  }, [exerciseInfo]);

  return (
    <div className="backGround">
      <Header headerText="Exercise Information" />
      <List
        bordered
        style={{ backgroundColor: "white" }}
        dataSource={exerciseInfo}
        renderItem={(item) => (
          <List.Item>
            <ExerciseInfo exerciseInfo={item} date={date} userID={userID} />
          </List.Item>
        )}
      />
      <Divider>Calorie Consumption</Divider>
      <p className="infoNameText">Total Calorie:</p>
      <p className="infoCalorieText">{totalCalorie} kcal</p>
      <Affix offsetBottom={0}>
        <Button
          type="primary"
          style={{ width: "100%", height: "50px" }}
          onClick={() => {
            navigate("/exerciseDetailoPage", {
              state: {
                isAdd: true,
                exerciseInfo: {},
                date: date,
                userID: userID,
              },
            });
          }}
        >
          Add more exercise
        </Button>
      </Affix>
    </div>
  );
}
