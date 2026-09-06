export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesObject) {
      return Object.keys(employeesObject).length;
    },
  };
}
