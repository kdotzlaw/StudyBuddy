const jestConfig = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  transform: {
    "^.+\\.js$": "babel-jest",
    '^.+\\.tsx?$': [
      'ts-jest',
      {
        useESM: true,
      },
    ],
  },
}

export default jestConfig;