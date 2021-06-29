public class User {
    int userId;
    String userName;
    String userPwd;

    User() {

    }

    public User(int _userId) {
        userId = _userId;
    }

    public User(int _userId, String _userName, String _userPwd) {
        userId = _userId;
        userName = _userName;
        userPwd = _userPwd;
    }

    public static void main(String[] args) {
        User u1 = new User(1001);
        User u2 = new User(1002,"Sean", "123456");

        System.out.println(u1.userId);
        System.out.println(u2.userId + u2.userName);
    }

}
