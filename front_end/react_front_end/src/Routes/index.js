import LoginComponent from "../Pages/LoginPage/LoginCompoment";
import HomeComponent from "../Pages/HomePage/HomeComponent";
import SignUpComponent from "../Pages/SignUpPage/SignUpComponent";
import GetUserInfoPage from "../Pages/GetUserInfoPage/GetUserInfoPage";
import FoodPage from "../Pages/FoodInfoPage/FoodPage";
import FoodDetailPage from "../Pages/FoodDetailPage/FoodDetailPage";
import UserInfoPage from "../Pages/UserInfoPage/UserInfoPage";
import ExerciseInfoPage from "../Pages/ExerciseInfoPage/ExerciseInfoPage";
import ExerciseDetailPage from "../Pages/ExerciseDetailPage/ExerciseDetailPage";

export default [
  {
    path: "/",
    element: <HomeComponent />,
  },
  {
    path: "/login",
    element: <LoginComponent />,
  },
  {
    path: "/signUp",
    element: <SignUpComponent />,
  },
  {
    path: "/foodPage",
    element: <FoodPage />,
  },
  {
    path: "/getUserInfoPage",
    element: <GetUserInfoPage />,
  },
  {
    path: "/foodDetailPage",
    element: <FoodDetailPage />,
  },
  {
    path: "/userInfoPage",
    element: <UserInfoPage />,
  },
  {
    path: "/exerciseInfoPage",
    element: <ExerciseInfoPage />,
  },
  {
    path: "/exerciseDetailoPage",
    element: <ExerciseDetailPage />,
  },
];
