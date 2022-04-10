// import COLORS from '../utils/colors'

import styled from '@emotion/styled'
import { AppBar, Box, Container, Grid } from '@mui/material';

const chosenCourses = [
  {
    title: 'MKTG101',
    desc: 'Introduction to Marketing',
  },
  {
    title: 'STAT430',
    desc: 'Probability',
  },
]


export default function PennSched() {
  return (
    <Box sx={{
      width: '100vw',
      height: '100vh',
      overflowY: 'hidden'
    }}>
      <Grid container spacing={1} sx={{ backgroundColor: 'light-gray', height: '100vh' }}>
        <Grid item xs={12} sx={{
          backgroundColor: 'red',
          height: '10%'
        }}>
          header
        </Grid>
        <Grid item container xs={12} spacing={2} sx={{
          height: '90%'
        }}>
          <Grid item xs={6} sm={3}>
            <Box sx={{ height: '100%', backgroundColor: 'red', ml: '16px' }}>
              test
            </Box>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Box sx={{ height: '100%', backgroundColor: 'red', xs: { mr: '16px' }, sm: { mr: '0' } }}>
              test
            </Box>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Box sx={{ height: '100%', backgroundColor: 'red', mr: '16px' }}>
              test
            </Box>
          </Grid>
        </Grid>
      </Grid>
    </Box>
  )
}