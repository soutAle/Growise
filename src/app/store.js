import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../frontend/features/auth/slices/authSlice';


export const store = configureStore({
    reducer: {
        auth: authReducer,
    },
});