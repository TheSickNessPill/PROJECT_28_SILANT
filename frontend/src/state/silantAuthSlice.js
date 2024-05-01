import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    token:"",
    access: ""
}

const silantAuthSlice = createSlice({
    name: "silantAuthSlice",
    initialState,
    reducers: {}
});

export const {} = silantAuthSlice.actions;
export default silantAuthSlice.reducer;