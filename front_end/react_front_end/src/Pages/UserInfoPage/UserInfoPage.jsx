import React, { useEffect, useState } from "react";
import {
  Avatar,
  Row,
  Col,
  Card,
  List,
  Skeleton,
  Typography,
  DatePicker,
} from "antd";
import { UserOutlined } from "@ant-design/icons";
import { useLocation, Link } from "react-router-dom";
import axios from "axios";
import moment from "moment";
import Header from "../../Components/Header/Header";
import "../../UniversalStyle/UniversalStyle.css";

export default function UserInfoPage() {
  const { state } = useLocation();
  const { userID } = state;
  const [chosenDate, setChosenDate] = useState(moment().format("YYYY-MM-DD"));
  const [userData, setUserData] = useState({});
  const [mealInfo, setMealInfo] = useState([]);
  const [exerciseInfo, setExerciseInfo] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [userName, setUserName] = useState("");
  const [remainedCalorie, setRemainedCalorie] = useState(0);
  const [BMR, setBMR] = useState(0);
  const [advice, setAdvice] = useState("");

  async function getInfo() {
    const userInfo = await axios.post("/getUserInfo/" + userID, {
      date: chosenDate,
    });
    const lastInfo = await axios.get("/get_last_UserInfo/" + userID);
    const dietInfo = await axios.post("/getDietLogs/" + userID, {
      date: chosenDate,
    });
    const sportInfo = await axios.post("/getExerciseLogs/" + userID, {
      date: chosenDate,
    });
    const adviceInfo = await axios.post("/getAdvice/" + userID, {
      date: chosenDate,
    });
    setAdvice(adviceInfo.data.advice);
    const realUserInfo = JSON.parse(userInfo.data);
    if (realUserInfo[0].isNone) {
      setUserData(lastInfo.data);
    } else {
      setUserData(realUserInfo.data);
    }
    console.log(dietInfo.data, sportInfo.data);
    if (dietInfo.data.isNone) {
      setMealInfo([]);
    } else {
      setMealInfo(dietInfo.data);
    }
    if (sportInfo.data.isNone) {
      setExerciseInfo([]);
    } else {
      setExerciseInfo(sportInfo.data);
    }
    setIsLoading(false);
  }

  useEffect(() => {
    setIsLoading(true);
    getInfo();
  }, [chosenDate]);

  useEffect(() => {
    if (userData) {
      setUserName(userData.userName);
      setBMR(userData.BMR);
    }
  }, [userData]);

  useEffect(() => {
    let tmp = BMR;
    mealInfo.map((item) => {
      tmp -= item.calorie_cost;
    });
    exerciseInfo.map((item) => {
      tmp += item.calorie;
    });
    setRemainedCalorie(tmp);
  }, [mealInfo, exerciseInfo]);

  function onDateChange(date, dateString) {
    setChosenDate(dateString);
  }

  return (
    <div style={{ overflowY: "scroll" }}>
      <Header headerText="User Info" />
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
        <Row align="middle">
          <Col span={8}>
            <Avatar
              icon={<UserOutlined />}
              src="https://joeschmoe.io/api/v1/random"
              size={64}
              style={{ marginTop: "20px", marginBottom: "20px" }}
            />
          </Col>
          <Col span={8} className="shownText" style={{ textAlign: "left" }}>
            Hello, <br /> {userName}
          </Col>
          <Col span={8} style={{ textAlign: "left" }}>
            <Link
              style={{ color: "royalblue" }}
              to="/getUserInfoPage"
              state={{ userID: userID, userData: userData }}
            >
              View My Info
            </Link>
          </Col>
        </Row>
        <DatePicker
          placeholder="Please Input the Date"
          size="large"
          defaultValue={moment(chosenDate, "YYYY-MM-DD")}
          style={{ width: "80%", marginTop: "30px", marginBottom: "30px" }}
          onChange={onDateChange}
        ></DatePicker>
        <Card
          title="Remaining Calorie"
          type="inner"
          style={{
            width: "90%",
            marginLeft: "5%",
            marginRight: "5%",
            marginTop: "30px",
            marginBottom: "30px",
            textAlign: "center",
            fontSize: "50px",
            fontWeight: "bolder",
            color: "#2F4F4F",
          }}
          headStyle={{ textAlign: "left" }}
        >
          {remainedCalorie} kcal
        </Card>
        <Card
          title="Your Advice"
          type="inner"
          style={{
            width: "90%",
            marginLeft: "5%",
            marginRight: "5%",
            marginTop: "30px",
            marginBottom: "30px",
            textAlign: "left",
            fontWeight: "bolder",
            color: "#2F4F4F",
          }}
          headStyle={{ textAlign: "left" }}
        >
          <Typography.Paragraph>{advice}</Typography.Paragraph>
        </Card>
        <Card
          title="My Meal"
          type="inner"
          style={{
            width: "90%",
            marginLeft: "5%",
            marginRight: "5%",
            marginTop: "30px",
            marginBottom: "30px",
            textAlign: "left",
          }}
          headStyle={{ textAlign: "left" }}
          extra={
            <Link
              style={{ color: "royalblue" }}
              to="/foodPage"
              state={{ date: chosenDate, userID: userID }}
            >
              View All
            </Link>
          }
        >
          <List
            size="small"
            dataSource={
              mealInfo.length === 1 && mealInfo[0].isNone ? [] : mealInfo
            }
            renderItem={(item) => {
              return <List.Item>{item.food_name}</List.Item>;
            }}
          />
        </Card>
        <Card
          title="My Exercise"
          type="inner"
          style={{
            width: "90%",
            marginLeft: "5%",
            marginRight: "5%",
            marginTop: "30px",
            marginBottom: "30px",
            textAlign: "left",
          }}
          headStyle={{ textAlign: "left" }}
          extra={
            <Link
              style={{ color: "royalblue" }}
              to="/exerciseInfoPage"
              state={{ date: chosenDate, userID: userID }}
            >
              View All
            </Link>
          }
        >
          <List
            size="small"
            dataSource={
              exerciseInfo.length === 1 && exerciseInfo[0].isNone
                ? []
                : exerciseInfo
            }
            renderItem={(item) => <List.Item>{item.exercise_name}</List.Item>}
          />
        </Card>
      </Skeleton>
    </div>
  );
}
