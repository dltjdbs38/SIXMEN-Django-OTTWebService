import React, { useState } from "react";
import { Button } from "../components";
import { theme } from "styled-tools";
import styled from "styled-components";
// import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { client } from "../libs";

export default function Create() {
  const navigate = useNavigate();
  const [board, setBoard] = useState({
    published_date: "",
    title: "",
    theater_owner: "",
    theater_genre1: "",
    theater_genre2: "",
    introduce: "",
    notice: "",
  });
  const { title, theater_owner, theater_genre1, theater_genre2, introduce, notice } = board;
  const onChange = (event) => {
    const { value, name } = event.target;
    setBoard({
      ...board,
      [name]: value,
    });
  };
  const saveBoard = async () => {
    await client.post(`small-theater`, board).then(() => {
      alert("소극장이 등록되었습니다.");
      navigate("/theater_list");
    });
  };
  // const saveBoard = async () => {
  //   await axios.post(`small-theater`, board).then((res) => {
  //     alert('소극장이 등록되었습니다.');
  //     navigate('/theater_list');
  //   });
  // };
  return (
    <Wrapper>
      <InputWrapper>
        <div>
          <span>소극장 제목 </span>
          <Input type="text" name="title" value={title} onChange={onChange} />
        </div>
        <br />
        <div>
          <span>작성자 </span>
          <Input type="text" name="theater_owner" value={theater_owner} onChange={onChange} />
        </div>
        <br />
        <div>
          <span>영화 장르1 </span>
          <Input type="text" name="theater_genre1" value={theater_genre1} onChange={onChange} />
        </div>
        <br />
        <div>
          <span>영화 장르2 </span>
          <Input type="text" name="theater_genre2" value={theater_genre2} onChange={onChange} />
        </div>
      </InputWrapper>
      <br />
      <div>
        <span>소극장 소개 </span>
        <TextArea name="introduce" cols="70" rows="35" value={introduce} onChange={onChange}></TextArea>
      </div>
      <div>
        <span>공지사항 </span>
        <TextArea name="notice" cols="70" rows="35" value={notice} onChange={onChange}></TextArea>
      </div>
      <div>
        <Button isMini={true} onClick={saveBoard}>
          소극장 생성하기
        </Button>
        <Button isMini={true} onClick={() => navigate("/theater_list")}>
          돌아가기
        </Button>
      </div>
    </Wrapper>
  );
}

const Wrapper = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 12rem;
  padding-bottom: 50rem;
  color: ${theme("colors.mainPoint")};
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}

  & > span {
    text-align: center;
  }
`;

const InputWrapper = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5rem;
  width: 144rem;
  color: ${theme("colors.mainPoint")};
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH2")}

  & > form {
    display: flex;
    align-items: center;
  }
`;

const Input = styled.input`
  width: 200px;
  height: 30px;
  font-size: 20px;
  ${theme("fonts.textH3")}
  font-family: NotoSerif;
  background-color: #ffffff;
`;

const TextArea = styled.textarea`
  width: 400x;
  height: 300px;
  font-size: 20px;
  ${theme("fonts.textH3")}
  font-family: NotoSerif;
  background-color: #ffffff;
`;
