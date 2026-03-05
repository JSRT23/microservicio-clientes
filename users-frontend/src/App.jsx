import { gql } from "@apollo/client";
import { useQuery, useMutation } from "@apollo/client/react";
import { useState } from "react";

/* QUERY TODOS LOS USUARIOS */

const GET_USERS = gql`
  query {
    allUsers {
      id
      name
      email
      phone
    }
  }
`;

/* MUTATION CREAR USUARIO */

const CREATE_USER = gql`
  mutation ($name: String!, $email: String!, $phone: String!) {
    createUser(name: $name, email: $email, phone: $phone) {
      user {
        id
        name
        email
        phone
      }
    }
  }
`;

function App() {
  const { loading, data, refetch } = useQuery(GET_USERS);

  const [createUser] = useMutation(CREATE_USER);

  const [searchId, setSearchId] = useState("");
  const [user, setUser] = useState(null);

  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
  });

  /* REGISTRAR USUARIO */

  const handleSubmit = async (e) => {
    e.preventDefault();

    await createUser({
      variables: form,
    });

    refetch();

    setForm({
      name: "",
      email: "",
      phone: "",
    });
  };

  /* BUSCAR USUARIO */

  const searchUser = async () => {
    const response = await fetch("http://localhost:8000/graphql/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: `
        query{
          user(id:${searchId}){
            id
            name
            email
            phone
          }
        }
        `,
      }),
    });

    const result = await response.json();
    setUser(result.data.user);
  };

  return (
    <div className="container mt-4">
      <h2 className="text-center mb-4">Microservicio de Usuarios</h2>

      {/* REGISTRO */}

      <div className="card mb-4">
        <div className="card-header">Registrar Cliente</div>

        <div className="card-body">
          <form onSubmit={handleSubmit}>
            <input
              className="form-control mb-2"
              placeholder="Nombre"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
            />

            <input
              className="form-control mb-2"
              placeholder="Email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />

            <input
              className="form-control mb-2"
              placeholder="Teléfono"
              value={form.phone}
              onChange={(e) => setForm({ ...form, phone: e.target.value })}
            />

            <button className="btn btn-primary">Registrar</button>
          </form>
        </div>
      </div>

      {/* BUSCAR */}

      <div className="card mb-4">
        <div className="card-header">Buscar Cliente</div>

        <div className="card-body">
          <input
            className="form-control mb-2"
            placeholder="ID Usuario"
            value={searchId}
            onChange={(e) => setSearchId(e.target.value)}
          />

          <button className="btn btn-success" onClick={searchUser}>
            Buscar
          </button>

          {user && (
            <div className="mt-3">
              <h5>Resultado</h5>

              <p>
                <b>Nombre:</b> {user.name}
              </p>

              <p>
                <b>Email:</b> {user.email}
              </p>

              <p>
                <b>Teléfono:</b> {user.phone}
              </p>
            </div>
          )}
        </div>
      </div>

      {/* LISTA USUARIOS */}

      <div className="card">
        <div className="card-header">Clientes Registrados</div>

        <div className="card-body">
          {loading ? (
            "Cargando..."
          ) : (
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Email</th>
                  <th>Teléfono</th>
                </tr>
              </thead>

              <tbody>
                {data.allUsers.map((user) => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.phone}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
