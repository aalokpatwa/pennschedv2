import React from "react";
import styled from "@emotion/styled";

import CourseOption from "./CourseOption";

import COLORS from "../colors";



const CourseSearchWrapper = styled.div`
  background-color: ${COLORS.sectionBackground};
  flex: 1 0 0;
  border-radius: 20px;
`

const SearchBar = styled.input`
  background-color: ${COLORS.light};

  margin: 10px;
  border-radius: 10px;

  font-family: 'Open Sans';
`



interface Course {
  title: string;
  desc: string;
}

interface ChosenCourses extends Array<Course>{}

interface State {
  query: string;
  chosenCourses: ChosenCourses;
}


class CourseSearch extends React.Component<any, State> {
  constructor(props : any) {
    super(props);
    this.state = { query: "", chosenCourses: this.props.chosenCoursesInit };
  }

  setChosenCourses(newChosenCourses: ChosenCourses) {
    this.setState({ chosenCourses: newChosenCourses });
  }

  render() {
    return (
      <CourseSearchWrapper>
        <SearchBar type="text"/>
          {this.state.chosenCourses.map((v: { title: string; desc: string; }, i: number) => (
            <p>
              test
            </p>
          ))}
      </CourseSearchWrapper>
    )
  }
}

export default CourseSearch;