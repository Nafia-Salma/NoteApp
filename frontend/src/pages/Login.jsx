import Form from "../components/Form"

function Login() {
    return <Form route="/api/token/access/" method="login" />
}

export default Login
