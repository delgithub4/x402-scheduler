from fastapi.responses import JSONResponse


def success(
    data=None,
    message="Request completed successfully.",
    status_code=200,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
        },
    )


def error(
    message="An error occurred.",
    errors=None,
    status_code=400,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "errors": errors or [],
        },
    )
