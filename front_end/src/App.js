import './App.less';
import {useRoutes} from 'react-router-dom'
import routes from './Routes'

function App() {
  const element = useRoutes(routes)
  return (
    <div className="App">
        {element}
    </div>
  );
}

export default App;
