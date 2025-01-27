import { createSlice } from '@reduxjs/toolkit'

export const Counter = createSlice({
    name: 'counter',
    initialState: {
        value: 0
    },
    reducers: {
        increment: (state) => {
            state.value += 1
        },
        decrement: (state) => {
            state.value -= 1
        },
        reset: (state) => {
            state.value = 0
        },

    }

})
export const { increment, decrement, reset } = Counter.actions;
export default Counter.reducer;