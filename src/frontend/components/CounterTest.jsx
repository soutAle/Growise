import { useDispatch, useSelector } from "react-redux";
import { increment, decrement, reset } from "../../redux/slices/Counter.jsx";


export const CounterTest = () => {
    const counter = useSelector(state => state.counter.value);
    const dispatch = useDispatch();

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold text-center my-10">Counter</h1>
            <button className="bg-blue-200 rounded-md p-2 m-2" onClick={() => dispatch(increment())}>Increment</button>
            <button className="bg-red-200 rounded-md p-2 m-2" onClick={() => dispatch(decrement())}>Decrement</button>
            <button className="bg-green-200 rounded-md p-2 m-2" onClick={() => dispatch(reset())}>Reset</button>
            <p className="text-center text-2xl font-bold">{counter}</p>
        </div>
    )
}