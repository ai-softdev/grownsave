from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="User already exists"
)

IncorrectEmailOrPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is expired"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is absent"
)

IncorrectTokenException = HTTPException(
    status_code=401, detail="Incorrect token format"
)

UserIsNotPresentException = HTTPException(status_code=404, detail="User not found")

UserIsNotAdminException = HTTPException(status_code=403, detail="User is not admin")

ModelNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
)

NotPermissionException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to perform this action"
)

AlreadyPurchasedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Subscription is already purchased"
)

NoSubscriptionException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="User has no subscription"
)