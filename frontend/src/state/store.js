import { configureStore } from "@reduxjs/toolkit";

import silantSliceReduser from "./silantSlice.js";
import silantAuthSliceReduser from "./silantAuthSlice.js";

export const store = configureStore({
    reducer: {
        "silantSlice": silantSliceReduser,
        "silantAuthSlice": silantAuthSliceReduser
    }
});