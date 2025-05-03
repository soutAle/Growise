import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../frontend/features/auth/authSlice';


export const store = configureStore({
    reducer: {
        auth: authReducer,
    },
});