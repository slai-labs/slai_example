'use strict'

const { Box, Button, Container, CssBaseline } = MaterialUI

// instead should take average people per household

const initialInput = {
  latitude: 32.7157,
  longitude: -117.1611,
  housing_median_age: 46,
  total_rooms: 6000,
  total_bedrooms: 1000,
  population: 5000,
  households: 3000,
  median_income: 15,
}

const Calculator = (props) => {
  const [input, setInput] = React.useState(initialInput)
  const [result, setResult] = React.useState(null)

  const updateInput = (e, e2, e3) => {
    setInput({ ...input, [e.target.name]: e.target.value })
  }

  const fetchEstimate = async () => {
    const response = await fetch('/slai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(input),
    })
    const result = (await response.json())[0]
    setResult(result)
  }

  return (
    <Container>
      <CssBaseline />
      <h1>California Housing Price Estimator</h1>
      <div>
        {Object.keys(initialInput).map((key) => {
          return (
            <div>
              <label>{key}</label>
              <input
                key={key}
                type="text"
                name={key}
                value={input[key]}
                onChange={updateInput}
              />
            </div>
          )
        })}
      </div>

      <button
        onClick={() => {
          fetchEstimate()
        }}
      >
        Estimate
      </button>
      <h1>{result}</h1>
    </Container>
  )
}

const domContainer = document.querySelector('#calculator')
ReactDOM.render(React.createElement(Calculator), domContainer)
