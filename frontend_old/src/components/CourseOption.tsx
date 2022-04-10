import React from "react";
import styled from "@emotion/styled";


const CourseOptionContainer = styled.div`
  background: white;
  
  text-align: center;
  
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
  
  margin: 10px;
  border-radius: 10px;
  box-shadow: 2px 2px 7px #FFFFFF55;
`

const CourseOptionTitle = styled.p`
  font-size: 48px;
  font-family: 'Open Sans';
  font-weight: 600;
  letter-spacing: 0.04em;
  
  background: -webkit-linear-gradient(#FF4487, #FF4487 25%, #2C8DFF 75%, #2C8DFF);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  
  margin: -2px 25px -5px 25px;
`

const CourseOptionDesc = styled.p`
  font-size: 14px;
  font-family: 'Open Sans';
  font-weight: 300;
  letter-spacing: 0.03em;
  color: black;
  
  margin: -4px 10px 4px 10px;
`

interface CourseOptionProps {
  title: string;
  desc: string;
}

const CourseOption = ({ title, desc } : CourseOptionProps) => {   
  return (
    <CourseOptionContainer>
      <CourseOptionTitle>{title}</CourseOptionTitle>
      <CourseOptionDesc>{desc}</CourseOptionDesc>
    </CourseOptionContainer>
  );
}

export default CourseOption;