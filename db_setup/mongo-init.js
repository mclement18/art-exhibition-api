db.createUser(
  {
      user: "testuser",
      pwd: "testpass",
      roles: [
          {
              role: "readWrite",
              db: "test"
          }
      ]
  }
);
