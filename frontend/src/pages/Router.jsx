import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
  Comments,
  Contents,
  CreateArticle,
  CreateDone,
  CreateTheater,
  Landing,
  Login,
  Main,
  NotFound,
  RegisterDetail,
  RegisterDone,
  RegisterId,
  RegisterName,
  TheaterList,
  Theater,
} from ".";
import { Header } from "../components";

const Router = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/Register/name" element={<RegisterName />} />
        <Route path="/Register/id" element={<RegisterId />} />
        <Route path="/Register/detail" element={<RegisterDetail />} />
        <Route path="/Register/done" element={<RegisterDone />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Main" element={<Main />} />
        <Route path="/Contents" element={<Contents />} />
        <Route path="/TheaterList" element={<TheaterList />} />
        <Route path="/Theater" element={<Theater />} />
        <Route path="/CreateTheater" element={<CreateTheater />} />
        <Route path="/CreateDone" element={<CreateDone />} />
        <Route path="/Comments" element={<Comments />} />
        <Route path="/CreateArticle" element={<CreateArticle />} />
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
